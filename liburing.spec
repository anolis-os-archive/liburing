%define alicloud_base_release 3

Name: liburing
Version: 0.6
Release: 1.%{alicloud_base_release}%{?dist}.alnx
Summary: Linux-native io_uring I/O access library
License: (GPLv2 with exceptions and LGPLv2+) or MIT
Source: https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
Patch0: 0001-io_uring_get_sqe-always-use-khead.patch
Patch1: 0002-__io_uring_get_cqe-silence-signed-vs-unsigned-compar.patch
Patch2: 0003-Fix-32-bit-warnings-on-compile.patch
Patch3: 0004-Use-__off64_t-for-offsets.patch
Patch4: 0005-Use-uint64_t-for-splice-offsets.patch
Patch5: 0006-fix-build-on-musl-libc.patch
Patch6: 0007-fix-missing-include-sys-stat.h-in-src-include-liburi.patch
Patch7: 0008-update-io_uring.h-with-tee.patch
Patch8: 0009-preseve-wait_nr-if-SETUP_IOPOLL-is-set.patch
Patch9: 0010-update-wait_nr-to-account-for-completed-event.patch
Patch10: 0011-remove-duplicate-call-to-__io_uring_peek_cqe.patch
Patch11: 0012-Add-CQ-ring-flags-field.patch
Patch12: 0013-Add-helpers-to-set-and-get-eventfd-notification-stat.patch
Patch13: 0014-Check-cq-ring-overflow-status.patch
Patch14: 0015-test-cq-overflow-peek.patch
Patch15: 0016-io_uring_peek_batch_cqe-should-also-check-cq-ring-ov.patch
Patch16: 0017-test-cq-overflow-correct-error-condition.patch
Patch17: 0018-test-cq-full-correct-error-condition.patch
URL: https://git.kernel.dk/cgit/liburing/
BuildRequires: gcc

# Fails to build and therefore isn't supported upstream
ExcludeArch: armv7hl

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%autosetup -p1

%build
CFLAGS="${CFLAGS:-%__global_cflags}" ; export CFLAGS
LDFLAGS="${LDFLAGS:-%__global_ldflags}"; export LDFLAGS
./configure --prefix=%{_prefix} --libdir=/%{_libdir} --libdevdir=/%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir}

%make_build

%install
%make_install

%files
%attr(0755,root,root) %{_libdir}/liburing.so.*
%license COPYING

%files devel
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%exclude %{_libdir}/liburing.a
%{_libdir}/pkgconfig/*
%{_mandir}/man2/*

%changelog
* Thu Jul 16 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.6-1.3.alnx
- fix testcase failed

* Tue Jul 14 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.6-1.2.alnx
- fix io_uring io_uring_peek_cqe not check cq ring overflow

* Thu May 28 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.6-1.1.alnx
- update version to 0.6

* Thu Mar 5 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.3-1.4.alnx
- __io_uring_get_cqe: remove redundant wait_nr clear

* Wed Mar 4 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.3-1.3.alnx
- __io_uring_get_cqe: eliminate unnecessary io_uring_enter() syscalls

* Tue Feb 4 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.3-1.2
- fix test/accept-reuse.c compile error
- remove unsupported macros

* Tue Feb 4 2020 Chunmei Xu <xuchunmei@linux.alibaba.com> - 0.3-1.1
- Rebuild for Alibaba Cloud Linux

* Tue Jan 7 2020 Stefan Hajnoczi <stefanha@redhat.com> - 0.3-1
- Add IORING_OP_STATX
- Add IORING_OP_OPENAT/IORING_OP_CLOSE helpers
- Add prep helpers for IORING_OP_FILES_UPDATE and IORING_OP_FALLOCATE
- Add io_uring_prep_connect() helper
- Add io_uring_wait_cqe_nr()
- Add IORING_OP_ASYNC_CANCEL and prep helper

* Thu Oct 31 2019 Jeff Moyer <jmoyer@redhat.com> - 0.2-1
- Add io_uring_cq_ready()
- Add io_uring_peek_batch_cqe()
- Add io_uring_prep_accept()
- Add io_uring_prep_{recv,send}msg()
- Add io_uring_prep_timeout_remove()
- Add io_uring_queue_init_params()
- Add io_uring_register_files_update()
- Add io_uring_sq_space_left()
- Add io_uring_wait_cqe_timeout()
- Add io_uring_wait_cqes()
- Add io_uring_wait_cqes_timeout()

* Tue Jan 8 2019 Jens Axboe <axboe@kernel.dk> - 0.1
- Initial version
